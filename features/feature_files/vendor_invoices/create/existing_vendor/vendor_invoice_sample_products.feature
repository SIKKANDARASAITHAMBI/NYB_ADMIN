Feature:  Sample Products Inward from Existing Vendor with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Vendor Invoice",
    When I select the warehouse,
    When I select the vendor,
    When I Enter Vendor Invoice No,
#   When I Upload the Invoice,


  #Without discount tax, and other charges.
  Scenario: Create a vendor invoice with sample product(new combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
#    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,


  #Without discount tax, and other charges.
  Scenario: Create a vendor invoice with sample product(existing combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  @vendor_invoice_sample_products4
  #Without discount tax, and other charges.
  Scenario: Create a vendor invoice with sample product(existing and new combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,