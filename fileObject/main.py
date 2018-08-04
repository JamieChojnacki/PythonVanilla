# for small files :
# with open('text.txt') as file:  # with open - file is opened and closed while ended
#     print(file.name)
#     print(file.read())
#     file_content = file.readlines()
#     print(file_content)
#
#     """ lets get simple lines """
#     file_lines = file.readline()
#     for line in range(8):
#         print(file_lines, end='')
#         file_lines = file.readline()
#
#     for line in file:
#         print(line, end='')
#
#     # for bigger files :
#     """ lets not get rid of memory """
#     fsc = file.read(10)  # read 10 bytes
#     print(fsc)
#     fsc_2 = file.read(10)  # read another 10 bytes
#     print(fsc_2)
#
#     # if EOF method returns a empty string, so:
#     """ that works too """
#     while(fsc) > 0:
#         print(fsc, end='*')
#         fsc = file.read(10)  # check if EOF

# with open('text.txt') as f:
#     sizeToRead = 10
#     fileContent = f.read(sizeToRead)
#     print(fileContent, end='')
#
#     f.seek(0)
#     fileContent = f.read(sizeToRead)
#     print(fileContent)
#
#     print(f.tell())  # show current position in file

""" read and write mechanics """
with open('text.txt', 'r') as rf:
    with open('new_text.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
