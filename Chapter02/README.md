# Selenim核心技术

## Selenim 八大定位方法

1. `find_element_by_id` 唯一id
1. `find_element_by_name` 
1. `find_elements_by_name`
1. `find_element_by_link_text`
1. `find_element_by_partial_link_text`
1. `find_element_by_xpath` (可以通过浏览器开发人员工具右键复制xpath)
1. `find_element_by_tag_name` 
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