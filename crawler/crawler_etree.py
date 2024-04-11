from lxml import etree

html_data = '''
<div id="root">
  <div id="products">
    <div class="product">
      <div id="product_name">Dark Red Energy Potion</div>
      <div id="product_price">$4.99</div>
      <div id="product_rate">4.7</div>
      <div id="product_description">Bring out the best in your gaming performance.</div>
    </div>
  </div>
</div>
'''

# Parse the HTML data using lxml
root = etree.fromstring(html_data)

# Navigate through the document
for parent in root:
    print(f"Parent tag: {parent.tag}")
    for child in parent:
        print(f"Child tag: {child.tag}")
        for grandchild in child:
            print(f"Grandchild tag: {grandchild.tag}, Attribute: {grandchild.attrib}, Text: {grandchild.text}")

html_data = '<div type="product_rate" review_count="774">4.7</div>'

# Parse the HTML data using lxml
element = etree.fromstring(html_data)

# Get a specific attribute value
print(element.get("review_count"))

html_data = '''
<div id="products">
  <div class="product">
    <div id="product_name">Dark Red Energy Potion</div>
    <div class="pricing">
      <div>Price with discount: $4.99</div>
      <div>Price without discount: $11.99</div>
    </div>
    <div id="product_rate" review_count="774">4.7 out of 5</div>
    <div id="product_description">Bring out the best in your gaming performance.</div>
  </div>
</div>
'''

# Parse the HTML data using lxml
root = etree.fromstring(html_data)

# Iterate over the product div elements
for element in root.xpath("//div//div//div"):
    print(element.text)

# parse elements
name = root.xpath("//div[@id='product_name']/text()")[0]
discount_price = root.xpath("//div[contains(text(), 'with discount')]/text()")[0]
review_count = root.xpath("//div[@id='product_rate']/@review_count")[0]
pricing = root.xpath("//div/div/div/div/text()")

print('names is {}'.format(name))
print('discount_price is {}'.format(discount_price))
print('review_count is {}'.format(review_count))
print('pricing is {}'.format(pricing))

# get all the div elements
div_elements = root.cssselect("div div div")

# Iterate over the product div elements
for element in div_elements:
    print(element.text)

# match by a specific text value
normal_price = [element for element in div_elements if "without discount" in element.text][0].text
print(normal_price)

# match by an attribute value
rate = [element for element in div_elements if element.get("id") == "product_rate"][0].text
print(rate)
