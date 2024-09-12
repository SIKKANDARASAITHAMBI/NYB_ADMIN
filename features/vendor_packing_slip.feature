#Create vendor packing slip with valid dates

Feature: Vendor packing slip

    #Vendor Packing Slip -- @Valid = {Numeric, Alphabat, special character, alphanumeric and speciial char}
    #Inward Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
    #Damaged Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
    #Unit Price -- #Valid = 0-9999999 {10, 30, 100.22, 20.09, 0, 9999999}
    #Inward Quantity -- INWARD_QTY01, INWARD_QTY02, INWARD_QTY03, INWARD_QTY04, INWARD_QTY05, INWARD_QTY06
    #Damaged Quantity -- DAMAGED_QTY01, DAMAGED_QTY02, DAMAGED_QTY03, DAMAGED_QTY04, DAMAGED_QTY05, DAMAGED_QTY06
    #Unit Price -- UNIT_PRICE01, UNIT_PRICE02, UNIT_PRICE03, UNIT_PRICE04, UNIT_PRICE05, UNIT_PRICE06

  @smoke_test
  Scenario: To verify whether a user with create access can create a vendor
  packing slip with valid inputs, by taking products as inward
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
#    Then I choose the document type as "vendor packing slip",
#    Then I select the warehouse,
#    Then I select the vendor,
#    Then I enter a valid packing slip number(#Packing slip no -- NO01),
#    Then I upload the packing slip,
#    Then I add products,
#    Then I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
#    Then I click submit button.
    Then I navigated to the invoice and packing slip page,
#    Then I verify the Invoice & Packing Slip landing page URL,
    Then I verify the autopopulated dates in the listing,
    Then I click the "View" button for the created entry,
    Then I verify that all the displayed details are correct.
















#  @Add_sample
#  Scenario: To verify whether a user with create access can create a vendor
#  packing slip with valid inputs, by taking only new sample product as inward
#
#    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
#    Then I navigate to the Inventory module,
#    Then I verify the inventory module URL,
#    Then I choose the document type as "vendor packing slip",
#    Then I select the warehouse,
#    Then I select the vendor,
#    Then I enter a valid packing slip number(#Packing slip no -- NO01),
#    Then I upload the packing slip,
#    Then I click add sample product option,
#    Then I add new sample product,
#    Then I click is sample product,
#    Then I enter a valid product name,
#    Then I enter a valid flavor name,
#    Then I enter a valid size/weight variant,
#    Then I enter a valid price,
#    Then I click confirm button,
#    Then I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
#    Then I click submit button.
#
#  @Add_sample
#  Scenario: To verify whether a user with create access can create a vendor
#  packing slip with valid inputs, by taking only new sample product
#  (same product more than one, different batch number) as inward
#
#    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
#    Then I navigate to the Inventory module,
#    Then I verify the inventory module URL,
#    Then I choose the document type as "vendor packing slip",
#    Then I select the warehouse,
#    Then I select the vendor,
#    Then I enter a valid packing slip number(#Packing slip no -- NO01),
#    Then I upload the packing slip,
#    Then I click add sample product option,
#    Then I add new sample product,
#    Then I click is sample product,
#    Then I enter a valid product name,
#    Then I enter a valid flavor name,
#    Then I enter a valid size/weight variant,
#    Then I enter a valid price,
#    Then I click confirm button,
#    Then I click add sample product option,
#    Then I add new sample product,
#    Then I click is sample product,
#    Then I enter a valid product name,
#    Then I enter a valid flavor name,
#    Then I enter a valid size/weight variant,
#    Then I enter a valid price,
#    Then I click confirm button,
#    Then I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,
#    Then I click submit button.