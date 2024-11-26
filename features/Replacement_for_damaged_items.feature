Feature: Vendor Invoice
  @Replacement_for_damaged_items
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I choose the document type as "Replacement_for_damaged_items",
    Then I select the warehouse,
    Then I select the order_id,



