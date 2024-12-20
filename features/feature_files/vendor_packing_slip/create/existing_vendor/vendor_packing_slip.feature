#Vendor Packing Slip -- @Valid = {Numeric, Alphabat, special character, alphanumeric and speciial char}
    #Inward Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
    #Damaged Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
    #Unit Price -- #Valid = 0-9999999 {10, 30, 100.22, 20.09, 0, 9999999}
    #Inward Quantity -- INWARD_QTY01, INWARD_QTY02, INWARD_QTY03, INWARD_QTY04, INWARD_QTY05, INWARD_QTY06
    #Damaged Quantity -- DAMAGED_QTY01, DAMAGED_QTY02, DAMAGED_QTY03, DAMAGED_QTY04, DAMAGED_QTY05, DAMAGED_QTY06
    #Unit Price -- UNIT_PRICE01, UNIT_PRICE02, UNIT_PRICE03, UNIT_PRICE04, UNIT_PRICE05, UNIT_PRICE06

Feature: Product inward from existing vendor with vendor packing slip as document type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module and verified the landing page URL,
    Then I choose the document type as "Vendor Packing Slip", select warehouse, and select vendor,
    When I Enter packing slip number,
    When I upload the packing slip,
    When I add products,
    When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,

  @vendor_packing_slip1
  Scenario: Create a vendor packing slip with all the required details
    When I click submit button.
    Then I verify the Invoice & Packing Slip landing page URL,
    When I filter the document no,
    Then I verify that the document is successfully created and displayed,