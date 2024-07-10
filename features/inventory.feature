Feature: Verify the inventory module is working as expected

#Create vendor packing slip with valid dates
  Scenario: Verify whether can able to create a vendor packing slip with valid inputs as a user with create, edit, and view access
    Given I visit the Chote Kisan website and log in as a user with create, edit, and view access,
    Then I navigate to the Inventory module,
    Then I verify the inventory module URL,
    Then I choose the document type as "vendor packing slip",
    Then I select the warehouse,
    Then I select the vendor,
    Then I enter a valid packing slip number,
    Then I upload the packing slip,
    Then I add products,
    Then I enter a valid inward quantity,
    Then I enter a valid damaged quantity,
    Then I enter the unit price,
    Then I enter the batch number,
    Then I enter the expiry date.