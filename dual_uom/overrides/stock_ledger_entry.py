from erpnext.stock.doctype.stock_ledger_entry.stock_ledger_entry import StockLedgerEntry
import frappe
from erpnext.stock.utils import get_or_make_bin


class CustomStockLedgerEntry(StockLedgerEntry):
    def before_submit(self):
        doc = frappe.get_doc(self.voucher_type, self.voucher_no)
        bin_name = get_or_make_bin(self.item_code, self.warehouse)
        bin = frappe.get_doc("Bin", bin_name)
        for item in doc.items:
            if self.item_code == item.item_code :
                try:
                    if self.warehouse == item.t_warehouse or self.warehouse == item.s_warehouse :
                        if self.actual_qty < 0 :
                            self.qty_2_change = item.qty2 * -1
                        else :
                            self.qty_2_change = item.qty2

                except Exception as e:
                    if self.warehouse == item.warehouse :
                        if self.actual_qty < 0 :
                            self.qty_2_change = item.qty2 * -1
                        else :
                            self.qty_2_change = item.qty2

        self.qty_2_after_transaction = bin.actual_quantity_2 + self.qty_2_change
        bin.actual_quantity_2 = self.qty_2_after_transaction
        bin.save()
