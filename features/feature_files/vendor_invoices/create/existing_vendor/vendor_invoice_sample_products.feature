Feature:  Sample Products from Existing Vendor with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Vendor Invoice",
    When I select the warehouse,
    When I select the vendor,
    When I Enter Vendor Invoice No,
    When I Upload the Invoice,
#    When I add products,

  #Without discount tax, and other charges.

  Scenario: Create a vendor invoice with sample product(new combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
#    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  Scenario: Create a vendor invoice with sample product(existing combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#   When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  Scenario: Create a vendor invoice with sample product(existing and new combination) as inward and without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#   When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  #Without tax, and other charges.
  Scenario: test
    When I enter discount amount,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
#   When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  Scenario: test1
    When I enter discount amount,
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#   When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  Scenario:
    When I enter discount amount,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,
    When I click add sample product option,
    When I add new sample products in existing combination,
    When I enter add new product, add new flavor, add new size weight(existing combination),
    When I click confirm button,
#   When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  #Without other charges.
  @testetst
  Scenario: yesttest
    When I enter tax amount,
    When I enter discount amount,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,


  #Without discount tax, and other charges.
  @testetst1
  Scenario: yesttest1
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,


  #Without tax, and other charges.

  @testetst2
  Scenario: yesttest2
    When I enter discount amount,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,


    #With other charges.

  @testetst3
  Scenario: yesttest3
    When I enter other charges,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,