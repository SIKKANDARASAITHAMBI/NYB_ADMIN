Feature: Create Order Normal Flow

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    #When I navigate to the Order module and verified the landing page URL,




  @create_order
  Scenario: Create order normal flow to place orders
    When I navigate to the Order module and verified the landing page URL,
    When I choose the company/branch type, shipping address, order date,
    Then I Verify the company/branch type, shipping address, order date,
    When I add Products,
    #Then I verify Products,
    Then I select Payment Mode,
    Then I click Submit Order,
    Then I verify the Order Received landing page URL,
    Then I Verify account name to submit order,
    Then I verify the Order placed success message,
    When I click Order Received Page,
    #Then I verify the Order Received landing page URL,
    Then I Enter Order ID,
    Then I click search2 button,
    Then Order ID Verify,
    Then I click view order,
    Then I click edit order,
    Then I click generate picking slip,
    Then I click edit order confirmation button,
    When I click download picking slip button,
   # Then I compare the edit order data with pdf data,
    When I click on picking slip & shipment preparation page,
    Then I click edit order & validate picking slip,
    Then I enter validation number,
    Then I enter Confirmation,
    Then I click proceed to shipment and document preparation,
    Then I click order out for delivery,
    Then I click Checkbox,
    Then I click move to delivered,









  #@order_received
  #Scenario: Order Received
  #  Then I verify the Order Received landing page URL,

   #Then
    #