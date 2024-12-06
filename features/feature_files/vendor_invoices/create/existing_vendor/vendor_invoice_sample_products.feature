Feature: Sample Products with Vendor Invoice as Document Type

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Vendor Invoice",
    When I select the warehouse,
    When I select the vendor,
    When I Enter Vendor Invoice No,
    When I Upload the Invoice,
    #When I add products,


    #When I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,


  #Without discount tax, and other charges.
  @vendor_invoice_sample_products
  #Scenario: Create a vendor invoice without discount, tax, or other charge
    Scenario: Add New Products with checkin and confirm

    When I click add sample product option,
    Then I add new sample product,
    Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,
    Then I click confirm button,


@vendor_invoice_sample_products2
    Scenario: Add New Products without checkin and confirm

    When I click add sample product option,
    Then I add new sample product,
    #Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,
    Then I click confirm button,

@vendor_invoice_sample_products3
    Scenario: Mixed of checkin and checkout in add new products and confirm

    When I click add sample product option,
    Then I add new sample product,
    Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,
    Then I add new sample product,
    #Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,


    Then I add new sample product,
    Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,

    Then I add new sample product,
   # Then I click is sample product,
    Then I enter a valid product name,
    Then I enter a valid flavor name,
    Then I enter a valid size/weight variant,
    Then I enter a valid price,
    Then I click confirm button,

