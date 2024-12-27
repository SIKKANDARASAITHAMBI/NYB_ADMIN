Feature: Product Inward & New sample Product from existing vendor with payment receipt as document type


Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    When I navigate to the Inventory module,
    Then I verify the Inventory module URL,
    When I choose the document type as "Payment_Reciept",
    When I select the warehouse,
    When I select the vendor,


  @payment_receipt1
  #Without discount tax, and other charges.
  Scenario: Create a payment receipt without discount, tax, or other charges
