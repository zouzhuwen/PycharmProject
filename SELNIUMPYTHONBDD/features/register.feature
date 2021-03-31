#coding=utf-8

Feature: Register User

  As a developer
  This is first bdd Project 这是第一个bdd项目

  Scenario: open register website
      When I open the register website
      Then I expect that the title is "注册"

  Scenario: input username
      When  I set with usermail "moshimoshi@163.com"
      And  I set with username "moshimoshi"
      And  I set with password "123456"
      And  I set with code "11111"
      And  I click with registerbutton
      Then I expect that text "验证码错误"