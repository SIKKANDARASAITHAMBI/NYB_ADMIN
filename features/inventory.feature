Feature: Verify the inventory module is working as expected

#Create vendor packing slip with valid dates
  Scenario: Verify whether can able to create a vendor packing slip with valid inputs as a user with create, edit, and view access

#Inward Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
#Damaged Quantity -- #Valid = 0-9999 {100, 1000, 5000, 9000}
#Inward Quantity -- INWARD_QTY01
#Damaged Quantity -- DAMAGED_QTY01

    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY01),
    Then I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY01),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.

#Inward Quantity -- INWARD_QTY02
#Damaged Quantity -- DAMAGED_QTY02

    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY02),
    Then I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY02),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.

#Inward Quantity -- INWARD_QTY03
#Damaged Quantity -- DAMAGED_QTY03

    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY03),
    Then I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY03),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.

#Inward Quantity -- INWARD_QTY04
#Damaged Quantity -- DAMAGED_QTY04

    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY04),
    Then I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY04),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.

#Inward Quantity -- INWARD_QTY05
#Damaged Quantity -- DAMAGED_QTY05

    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY05),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.

#Inward Quantity -- INWARD_QTY06
#Damaged Quantity -- DAMAGED_QTY06

    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY06),
    Then I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY06),
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.