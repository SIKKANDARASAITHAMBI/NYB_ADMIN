Feature: Product inward from new vendor with payment receipt as document type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Payment_Reciept",
    When I select the warehouse,
    When I select the new vendor,
    When I Enter vendor name,

  #Without discount tax, and other charges.
  Scenario: Create a payment receipt without discount, tax, or other charges
    When I enter Payment Receipt No1,
    When I enter Purchase Order No,
    When I upload the receipt,
    When I upload Document Proof For Discount,
    When I enter notes,
    When I Select the Payment Mode,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #Without tax, and other charges.
  Scenario: Create a vendor invoice with a discount but without tax or other charges
    When I enter Payment Receipt No2,
    When I enter Purchase Order No,
    When I upload the receipt,
    When I upload Document Proof For Discount,
    When I enter notes,
    When I Select the Payment Mode,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #Without other charges.
  Scenario: Create a vendor invoice with tax and discount but without other charges
    When I enter Payment Receipt No3,
    When I enter Purchase Order No,
    When I upload the receipt,
    When I upload Document Proof For Discount,
    When I enter notes,
    When I Select the Payment Mode,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I enter tax amount,
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,


  #All charges included
  Scenario: Create a vendor invoice with tax, discount and other charges
    When I enter Payment Receipt No4,
    When I enter Purchase Order No,
    When I upload the receipt,
    When I upload Document Proof For Discount,
    When I enter notes,
    When I Select the Payment Mode,
    When I add products,
    When I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I enter tax amount,
    When I enter other charges,
    When I enter discount amount,
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,