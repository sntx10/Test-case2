db = db.getSiblingDB('forms_db');

db.forms.insertMany([
  {
    "name": "MyForm",
    "fields": [
      {"name": "email", "type": "email"},
      {"name": "phone", "type": "phone"},
      {"name": "date", "type": "date"},
      {"name": "text_field", "type": "text"}
    ]
  },
  {
    "name": "OrderForm",
    "fields": [
      {"name": "customer_email", "type": "email"},
      {"name": "customer_phone", "type": "phone"},
      {"name": "order_date", "type": "date"},
      {"name": "order_details", "type": "text"}
    ]
  }
]);
