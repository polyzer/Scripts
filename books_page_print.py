def print_pages(page_count, print_set):
	filename = "page_count.txt"
	f = open(filename, "bw");
	full_sets_count = page_count // (print_set * 4) # это количество сетов для печати чтобы потом их склеить
	part_page_count = page_count % (print_set * 4) # сколько страниц не влезло
	round_part_page_count = part_page_count - (part_page_count % 4)
	
	k = 0 # смещение для страницы в проходе по сету
	i = 0
	j = 0
	while i < full_sets_count:
		k = 0
		while j < print_set:
#			print("%i,%i,", % ( i * (print_set * 4) + (print_set * 4) - k, i * (print_set * 4) + k + 1), file = f)
			f.write(bytes(""+str( i * (print_set * 4) + (print_set * 4) - k)+","+str(i * (print_set * 4) + k + 1)+",", "UTF-8"));
			k += 2
			j += 1
		i += 1
	k = 0
	i = 0
	j = 0
	while i < (round_part_page_count // 4):
#		print("%i,%i,", %(full_sets_count * (print_set * 4) + (round_part_page_count / 4) - k, full_sets_count * (print_set * 4) + (round_part_page_count / 4) + k + 1), file=f) # смещение на количество сетов
		f.write(bytes(""+str(full_sets_count * (print_set * 4) + round_part_page_count - k)+","+str(full_sets_count * (print_set * 4) + k + 1)+",", "UTF-8"))
		k += 2
		i += 1
		
	f.write(bytes("\n", "UTF-8"))

	k = 1 # смещение для страницы в проходе по сету
	i = 0
	j = 0
	while i < full_sets_count:
		k = 1
		while j < print_set:
#			print("%i,%i,", %(i * (print_set * 4) + k + 1,  i * (print_set * 4) + (print_set * 4) - k), file=f)
			f.write(bytes(""+str(i * (print_set * 4) + k + 1)+","+str(i * (print_set * 4) + (print_set * 4) - k)+",", "UTF-8"))
			k += 2
			j += 1
		i += 1
	k = 1
	i = 0
	j = 0
	while i < (round_part_page_count // 4):
#		print("%i,%i,", % ( full_sets_count * (print_set * 4) + (round_part_page_count / 4) + k + 1, full_sets_count * (print_set * 4) + (round_part_page_count / 4) - k), file=f) # смещение на количество сетов
		f.write(bytes(""+str( full_sets_count * (print_set * 4) + k + 1)+","+str(full_sets_count * (print_set * 4) + round_part_page_count - k)+",", "UTF-8"))
		k += 2
		i += 1
	f.write(bytes("\n", "UTF-8"))	
	if part_page_count != 0:
		f.write(bytes(""+str(full_sets_count * (print_set * 4) + round_part_page_count + 3)+",", "UTF-8"))
		f.write(bytes(""+str(full_sets_count * (print_set * 4) + round_part_page_count + 1)+",", "UTF-8"))
		f.write(bytes(""+str(full_sets_count * (print_set * 4) + round_part_page_count + 2), "UTF-8"))
	print("Номера страниц записаны в файл " + filename + "\n")

page_count = input("Введите количество страниц: ")
print_set = 10

print_pages( int(page_count), print_set)
