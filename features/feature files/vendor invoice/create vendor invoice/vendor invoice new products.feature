Feature: Product Inward from Existing Vendor with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Vendor Invoice",
    When I select the warehouse,
    When I select the vendor,
    When I Enter Vendor Invoice No,
    When I Upload the Invoice,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,


  #Without discount tax, and other charges.
  Scenario: Create a vendor invoice without discount, tax, or other charges
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #Without tax, and other charges.
  Scenario: Create a vendor invoice with a discount but without tax or other charges
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #Without other charges.
  Scenario: Create a vendor invoice with tax and discount but without other charges
    When I enter tax amount,
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #All charges included
  Scenario: Create a vendor invoice with tax, discount and other charges
    When I enter tax amount,
    When I enter other charges,
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,