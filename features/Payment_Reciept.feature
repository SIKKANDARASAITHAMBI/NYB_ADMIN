Feature: Vendor Invoice
  @Payment_Reciept
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I choose the document type as "Payment_Reciept",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter Payment Receipt No,
    Then I enter Purchase Order No,
    Then I upload the receipt,