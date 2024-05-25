from django import forms
from store.models import Item, IssueItem, ReturnItem


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['code', 'name', 'description', 'created_by', 'date_created']
        
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'code', 'description', 'created_by', 'date_created']
        

class IssueItemForm(forms.ModelForm):
    class Meta:
        model = IssueItem
        fields = ['item', 'issued_to', 'department', 'return_date']
        
class ReturnItemForm(forms.ModelForm):
    class Meta:
        model = ReturnItem
        fields = ['item', 'returned_date', 'returned_by']