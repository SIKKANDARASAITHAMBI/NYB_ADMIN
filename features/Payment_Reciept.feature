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
    Then I add products,
    Then I enter a valid Payment Receipt inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    Then I enter discounts,
    Then I enter tax,
    Then I enter other charges,
    Then I enter Document Proof For Discount,
    Then I enter notes,
    Then I Select the Payment Mode,
    Then I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,


  @integrate
  Scenario: Verify the items added in Vendor Invoices & Packing slips

    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    Then I navigate to vendor and inovice packing slip page,
    Then I verify the vendor and inovice packing slip page,
    Then I choose the document type as vsp "Payment_Reciept",





