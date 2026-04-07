Feature: Order transaction
  Tests related to order transactions

  Scenario Outline: Verify order success message shown in details page
    Given place the item order with "<userEmail>" and "<userPassword>"
    And the user is on landing page
    When I login to portal with "<userEmail>" and "<userPassword>"
    And navigate to orders page
    And select the orderId
    Then order message is successfully displayed

    Examples:
      | userEmail                 | userPassword |
      | 123bug456report@gmail.com | Coco2004!    |
      | dariart.design@gmail.com  | Coco2004!    |
