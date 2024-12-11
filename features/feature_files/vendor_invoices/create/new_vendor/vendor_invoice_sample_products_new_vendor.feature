Feature: Sample Product from New Vendor with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Vendor Invoice",
    When I select the warehouse,
    When I select the new vendor,
    When I Enter vendor name,
    When I Enter Vendor Invoice No,
    When I Upload the Invoice,

     #Without discount tax, and other charges.
  @testetst4
  Scenario: Create a vendor invoice without discount, tax, or other charges
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,

  @testetst5
  Scenario: Create a vendor invoice without discount, with tax, & other charges
    When I enter tax amount,
    When I enter other charges,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,

  @testetst6
  Scenario: Create a vendor invoice with discount, without tax, & other charges
    When I enter discount amount,
    When I enter other charges,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,

  @testetst7
  Scenario: Create a vendor invoice with discount, & other charges without tax,
    When I enter discount amount,
    When I enter other charges,
    When I click add sample product option,
    When I add new sample products,
    When I enter add new product, add new flavor, add new size weight(New combination),
    When I click confirm button,