from erpnext.stock.doctype.stock_ledger_entry.stock_ledger_entry import StockLedgerEntry
import frappe
class CustomStockLedgerEntry(StockLedgerEntry):
    def before_submit(self):
        doc = frappe.get_doc(self.voucher_type, self.voucher_no)
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
