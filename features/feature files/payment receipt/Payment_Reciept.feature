Feature: Vendor Invoice
  @Payment_Reciept
  Scenario: Create and verify vendor Invoice
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    When I verify the Inventory module URL,
    When I choose the document type as "Payment_Reciept",
    When I select the warehouse,
    When I select the vendor,
    When I enter Payment Receipt No,
    When I enter Purchase Order No,
    When I upload the receipt,
    When I add products,
    When I enter a valid Payment Receipt inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
    When I enter discounts,
    When I enter tax,
    When I enter other charges,
    When I enter Document Proof For Discount,
    When I enter notes,
    When I Select the Payment Mode,
    When I click submit button.
    When I verify the Invoice & Packing Slip landing page URL,


  @integrate
  Scenario: Verify the items added in Vendor Invoices & Packing slips

    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    When I verify the Inventory module URL,
    When I navigate to vendor and inovice packing slip page,
    When I verify the vendor and inovice packing slip page,
    When I choose the document type as vsp "Payment_Reciept",





