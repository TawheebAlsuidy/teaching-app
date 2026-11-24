with open('/mnt/sdcard/projects/teaching-app/chem-lab/transform_app.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_block = """    expReviewBtn = '<button class="qo" style="background:var(--acc-dark);color:#fff!important;margin-top:8px;text-align:center" onclick="reviewLinkedExp(&quot;' + q.expId + '&quot;, ' + (q.page || 'null') + ')">⚗️ راجع التجربة في المعمل والكتاب</button>';
  if (q.expId) {
    expReviewBtn = '<button class="qo" style="background:var(--acc-dark);color:#fff!important;margin-top:8px;text-align:center" onclick="reviewLinkedExp(&quot;' + q.expId + '&quot;, ' + (q.page || 'null') + ')">⚗️ راجع التجربة في المعمل والكتاب</button>';
      '⚗️ راجع التجربة في المعمل والكتاب</button>';
  }"""

good_block = """  let expReviewBtn = '';
  if (q.expId) {
    expReviewBtn = '<button class="qo" style="background:var(--acc-dark);color:#fff!important;margin-top:8px;text-align:center" onclick="reviewLinkedExp(&quot;' + q.expId + '&quot;, ' + (q.page || 'null') + ')">⚗️ راجع التجربة في المعمل والكتاب</button>';
  }"""

text = text.replace(bad_block, good_block)

# Fix function declaration
text = text.replace(
    'function reviewLinkedExp(&quot;\' + q.expId + \'&quot;, \' + (q.page || \'null\') + \') {',
    'function reviewLinkedExp(expId, pageNum) {'
)

with open('/mnt/sdcard/projects/teaching-app/chem-lab/transform_app.py', 'w', encoding='utf-8') as f:
    f.write(text)
