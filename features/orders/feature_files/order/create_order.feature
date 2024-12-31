Feature: Create Order Normal Flow

  Background:
    Given I visit the NYB admin website and log in as a user with create, edit, and view access,
    #When I navigate to the Order module and verified the landing page URL,




  @create_order
  Scenario: Create order normal flow to place orders
    When I navigate to the Order module and verified the landing page URL,
    When I choose the company/branch type, shipping address, order date,
    When I add Products,
    Then I select Payment Mode,
    Then I click Submit Order,
    Then I verify the Order Received landing page URL,
    Then I Verify account name to submit order,
    Then I verify the Order placed success message,
    When I click Order Received Page,
    #Then I verify the Order Received landing page URL,
    Then I Enter Order ID,

  #@order_received
  #Scenario: Order Received
  #  Then I verify the Order Received landing page URL,

   #Then
    #When I choose the company/branch
    #When I add products,
    #When I select payment mode,




    