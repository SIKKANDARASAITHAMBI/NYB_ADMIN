Feature: Product Inward from Existing Vendor with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module and verified the landing page URL,
    When I choose the document type as "Vendor Invoice", select warehouse, and select vendor
    Then I verify the choosed document type, warehouse , and vendor,
    When I Enter Vendor Invoice No,
    When I Upload the Invoice,
#    When I enter notes,
#    When I add Document Proof For Discount,
    When I add products,
    Then I verify the added products
    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  @testtttttt
  #Without discount tax, and other charges.
  Scenario: Create a vendor invoice without discount, tax, or other charges
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,