st = '1' * 10

while '111' in st or '888' in st:
    if '111' in st:
       st = st.replace('111','88', 1)
    else:
         st = st.replace('88888','8', 1)

print(st)

# st = '111111111'
# st = '88111111'
# st = '8888111'
# st = '8888881'
# st = '881'
