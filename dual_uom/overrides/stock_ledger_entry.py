from erpnext.stock.doctype.stock_ledger_entry.stock_ledger_entry import StockLedgerEntry
import frappe
from erpnext.stock.utils import get_or_make_bin


class CustomStockLedgerEntry(StockLedgerEntry):
    def before_submit(self):
        doc = frappe.get_doc(self.voucher_type, self.voucher_no)
        bin_name = get_or_make_bin(self.item_code, self.warehouse)
        bin = frappe.get_doc("Bin", bin_name)
        if self.voucher_type == "Stock Reconciliation":
            if self.actual_qty == 0 and self.actual_qty == 0 :
                bin.actual_quantity_2 = 0
                bin.save(ignore_permissions=True,  ignore_links=True)
            else :
                for item in doc.items:
                    if self.item_code == item.item_code and self.warehouse == item.warehouse :
                        self.qty_2_change = item.qty2
                        self.qty_2_after_transaction = self.qty_2_change
                        bin.actual_quantity_2 = self.qty_2_change
                        bin.save(ignore_permissions=True,  ignore_links=True)
        else :
            for item in doc.items:
                if self.item_code == item.item_code :
                    try:
                        if self.warehouse == item.t_warehouse or self.warehouse == item.s_warehouse :
                            if self.actual_qty < 0 :
                                self.qty_2_change = -item.qty2
                            else :
                                self.qty_2_change = item.qty2

                    except:
                        if self.warehouse == item.warehouse :
                            if self.actual_qty < 0 :
                                self.qty_2_change = -item.qty2
                            else :
                                self.qty_2_change = item.qty2
            self.qty_2_after_transaction = bin.actual_quantity_2 + self.qty_2_change
            bin.actual_quantity_2 = self.qty_2_after_transaction
            bin.save(ignore_permissions=True,  ignore_links=True)
