Feature: Vendor Invoice
  @vendor_invoice
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I choose the document type as "Vendor Invoice",
    Then I select the warehouse,
    Then I select the vendor,
    Then I Enter Vendor Invoice No,
    Then I Upload the Invoice,
    Then I add products,
    Then I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    Then I click submit button.





