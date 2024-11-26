Feature: Vendor Invoice
  @IntrawarehouseTransferInvoice
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I choose the document type as "IntrawarehouseTransfer Invoice",
    Then I select the from warehouse,
    Then I select the to warehouse,
    Then I enter the number,
    Then Upload the Transfer Invoice,
    Then I add products,
    Then I enter a valid Intrawarehouse inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    Then I click submit button.