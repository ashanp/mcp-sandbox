
from typing import Any
import hashlib
from loguru import logger
from mcp.server.fastmcp import FastMCP
import xml.etree.ElementTree as ET


# Load untitled.xml at startup
xml_path = "untitled.xml"
try:
    tree = ET.parse(xml_path)
    xml_root = tree.getroot()
    print(f"[DEBUG] XML loaded at startup. Root tag: {xml_root.tag}")
except Exception as e:
    print(f"[ERROR] Failed to load XML at startup: {e}")
    xml_root = None

# Function to read and parse untitled.xml (from loaded xml_root)
def read_xml():
    if xml_root is None:
        print(f"[ERROR] XML not loaded.")
        return None
    sections = {}
    for section in xml_root:
        print(f"[DEBUG] Section: {section.tag}")
        sections[section.tag] = ET.tostring(section, encoding='unicode')
    return sections

mcp = FastMCP("public-demo")

@mcp.tool()
def getCurrentSummary():
    if xml_root is None:
        print(f"[ERROR] XML not loaded.")
        return []
    # Navigate to InvoiceTotals > CurrentCharges > CurrentSummary
    invoice_totals = xml_root.find('InvoiceTotals')
    if invoice_totals is None:
        print("[ERROR] <InvoiceTotals> not found")
        return []
    current_charges = invoice_totals.find('CurrentCharges')
    if current_charges is None:
        print("[ERROR] <CurrentCharges> not found")
        return []
    current_summary = current_charges.find('CurrentSummary')
    if current_summary is None:
        print("[ERROR] <CurrentSummary> not found")
        return []
    summary_list = []
    for det in current_summary.findall('Det'):
        # Convert attributes to dict
        summary_list.append(det.attrib)
    return summary_list


@mcp.tool()
def get_plan_addons_devices():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Plan, Add-ons & Devices")]

@mcp.tool()
def get_out_of_plan_usage_charges():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Out of plan usage charges")]

@mcp.tool()
def get_one_time_charges():
    return [det.attrib for det in _get_currentsummary_dets_by_description("One-time charges")]

@mcp.tool()
def get_promotions_refunds_adjustments():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Promotions, Refunds & Adjustments")]

@mcp.tool()
def get_value_added_services_vas_3rd_party_charges():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Value added services (VAS) & 3rd party charges")]

@mcp.tool()
def get_vat_on_taxable_services():
    return [det.attrib for det in _get_currentsummary_dets_by_description("VAT on taxable services")]

@mcp.tool()
def get_current_month_charges_including_vat_5():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Current month charges (including VAT 5%)")]

@mcp.tool()
def get_payment_due_by():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Payment Due By")]

@mcp.tool()
def get_grand_total_incl_5_vat():
    return [det.attrib for det in _get_currentsummary_dets_by_description("Grand total (Incl 5% VAT)")]

# Helper function to get <Det> elements by Description in <CurrentSummary>
def _get_currentsummary_dets_by_description(description):
    if xml_root is None:
        return []
    invoice_totals = xml_root.find('InvoiceTotals')
    if invoice_totals is None:
        return []
    current_charges = invoice_totals.find('CurrentCharges')
    if current_charges is None:
        return []
    current_summary = current_charges.find('CurrentSummary')
    if current_summary is None:
        return []
    return [det for det in current_summary.findall('Det') if det.attrib.get('Description') == description]

@mcp.tool()
def generate_md5_hash(input_str: str) -> str:
    logger.info(f"Generating MD5 hash for: {input_str}")
    print(f"[DEBUG] Generating MD5 hash for: {input_str}")
    md5_hash = hashlib.md5()
    md5_hash.update(input_str.encode('utf-8'))
    return md5_hash.hexdigest()

@mcp.tool()
def count_characters(input_str: str) -> int:
    logger.info(f"Counting characters in: {input_str}")
    print(f"[DEBUG] Counting characters in: {input_str}")
    return len(input_str)

@mcp.tool()
def get_first_half(input_str: str) -> str:
    logger.info(f"Getting first half of: {input_str}")
    print(f"[DEBUG] Getting first half of: {input_str}")
    midpoint = len(input_str) // 2
    return input_str[:midpoint]

@mcp.tool()
def echo(input_data: Any) -> Any:
    logger.info(f"Echoing data: {input_data}")
    print(f"[DEBUG] Echoing data: {input_data}")
    return input_data + "from Ashan"

if __name__ == "__main__":
    mcp.run(transport='stdio')
