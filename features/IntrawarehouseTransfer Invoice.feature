Feature: Vendor Invoice
  @vendor_invoice
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I choose the document type as "IntrawarehouseTransfer Invoice",
    Then I select the from warehouse
    Then I select the recieving warehouse
    Then Upload the Transfer Invoice