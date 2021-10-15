# Selenim核心技术

## Selenim 八大定位方法

1. `find_element_by_id` 唯一id
1. `find_element_by_name` 通过 name 属性获取第一个元素
1. `find_elements_by_name` 通过 name 获取所有具有相同name的元素集合
1. `find_element_by_link_text` 通过链接里面的文本找到对应的a链接
1. `find_element_by_partial_link_text` 通过链接里面的部分文本找到对应的a链接
1. `find_element_by_xpath` (可以通过浏览器开发人员工具右键复制xpath)
1. `find_element_by_tag_name` 通过 tagName 获取元素
1. `find_element_by_css_selector` (可以通过浏览器开发人员工具右键复制selector)
1. `find_element_by_class_name` 通过className定位元素
1. `find_element` 综合方法 修改综合方法默认参数需要倒入 `from selenium.webdriver.common.by import By`

selenium.webdriver.common.by:

```python
CLASS_NAME = 'class name'
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link'
TAG_NAME = 'tag name'
XPATH = 'xpath'
```

## WebDriver 运行原理

参考打车🚖的案例

把 WebDriver 类比成司机
把 浏览器类比成车


WebDriver 实际上启动了一个服务通过 WebDriver 和 浏览器之间通过 http 协议通讯 （C/S结构）

## 掌握 WebDriver 核心方法和属性的使用

| # | 属性 | 属性描叙 |
|----|----|----|
| 1 | driver.name | 浏览器名称 |
| 2 | driver.current_url | 当前url |
| 3 | driver.title | 当前页面标题 |
| 4 | driver.page_source | 当前页面源码 |
| 5 | driver.current_window_handle | 窗口句柄 |
| 6 | driver.window_handles | 当前窗口所有句柄 |



| # | 方法 | 方法描叙 |
|----|----|----|
| 1 | driver.back() | 返回到上个页面 |
| 2 | driver.refresh() | 刷新当前页面 |
| 3 | driver.close() | 关闭当前页面 |
| 4 | driver.quit() | 关闭浏览器 |

## 掌握 WebElement 核心方法和属性的使用

[http://sahitest.com/demo](http://sahitest.com/demo)

这个链接提供了很多自动化测试需要用的页面

| # | 属性 | 属性描叙 |
|----|----|----|
| 1 | id | 标示 |
| 2 | size | 宽高 |
| 3 | rect | 宽高和坐标 |
| 4 | tag_name | 标签名称 |
| 5 | text | 文本内容 |


| # | 方法 | 方法描叙 |
|----|----|----|
| 1 | send_keys() | 输入内容 |
| 2 | clear() | 清空内容 |
| 3 | click()| 单击 |
| 4 | get_attribute() | 获得属性值 |
| 5 | is_selected() | 是否被选中 |
| 5 | is_enabled() | 是否可用 |
| 5 | id_displayed() | 是否显示 |
| 5 | value_of_css_property() | css属性值 |