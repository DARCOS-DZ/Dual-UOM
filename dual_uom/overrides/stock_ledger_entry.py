from erpnext.stock.doctype.stock_ledger_entry.stock_ledger_entry import StockLedgerEntry
import frappe
class CustomStockLedgerEntry(StockLedgerEntry):
    def before_submit(self):
        doc = frappe.get_doc(self.voucher_type, self.voucher_no)
        for child_doc in doc.items:
            if self.item_code == child_doc.item_code :
                try:
                    if self.warehouse == child_doc.t_warehouse or self.warehouse == child_doc.s_warehouse :
                        if self.actual_qty < 0 :
                            self.qty_2_change = child_doc.qty2 * -1
                        else :
                            self.qty_2_change = child_doc.qty2
                except Exception as e:
                    if self.warehouse == child_doc.warehouse :
                        if self.actual_qty < 0 :
                            self.qty_2_change = child_doc.qty2 * -1
                        else :
                            self.qty_2_change = child_doc.qty2
