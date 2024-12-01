Feature: Product Transfer Between Warehouses with Intra-Warehouse Transfer as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "IntrawarehouseTransfer Invoice",
    When I select the from warehouse,
    When I select the to warehouse,
    When I enter the number,
    When Upload the Transfer Invoice,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I click submit button.

  Scenario: Create and verify vendor Invoice
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,

