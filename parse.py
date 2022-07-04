from recipe_parser import Calorizator

recipe_links = Calorizator.parse_category(Calorizator.CATEGORIES[0])

recipe = Calorizator.get_recipe(recipe_links[0])
print(recipe)
print({'total': ['Итого', '1007', '87.3', '63', '32.4', '1070.5'],
       'one_hundred_grams': ['100 грамм', '100', '8.7', '6.3', '3.2', '106.3'],
       'one_portion': ['1 порция', '168', '14.6', '10.5', '5.4', '178.4'],
       'name_recipe': 'Азиатский салат с сырными шариками',
       'recipe_steps': '1. Нарезать курицу мелкими кубиками.\n2. Замариновать курицу в соевом соусе и оливковом масле, добавить перец и кунжут.\n3. Нарезать укроп.\n4. Замаринованную курицу обжарить до готовности.\n5. Фету смешать с нарезанным укропом, чесноком. Скатать небольшие шарики.\n6. Нарезать пекинскую капусту, перец и тонко нарезать лук.\n7. Для соуса смешать сметану с соком мандарина, соевым соусом и поперчить.\n8. В салатник выложить пекинскую капусту, нарезанный лук и болгарский перец.\n9. Выложить курицу и заправить салат.\n10. Перед подачей выложить сырные шарики.\n',
       'products': [{'mera': ' куриное филе', 'weight': ' куриное филе', 'protein_product': ' куриное филе',
                     'fat_product': ' куриное филе', 'carbohydrates_product': ' куриное филе',
                     'calories_product': ' куриное филе'},
                    {'mera': ' соус соевый', 'weight': ' соус соевый', 'protein_product': ' соус соевый',
                     'fat_product': ' соус соевый', 'carbohydrates_product': ' соус соевый',
                     'calories_product': ' соус соевый'},
                    {'mera': ' масло оливковое', 'weight': ' масло оливковое', 'protein_product': ' масло оливковое',
                     'fat_product': ' масло оливковое', 'carbohydrates_product': ' масло оливковое',
                     'calories_product': ' масло оливковое'},
                    {'mera': ' перец черный молотый', 'weight': ' перец черный молотый',
                     'protein_product': ' перец черный молотый', 'fat_product': ' перец черный молотый',
                     'carbohydrates_product': ' перец черный молотый', 'calories_product': ' перец черный молотый'},
                    {'mera': ' кунжут черный', 'weight': ' кунжут черный', 'protein_product': ' кунжут черный',
                     'fat_product': ' кунжут черный', 'carbohydrates_product': ' кунжут черный',
                     'calories_product': ' кунжут черный'},
                    {'mera': ' сыр фета', 'weight': ' сыр фета', 'protein_product': ' сыр фета',
                     'fat_product': ' сыр фета', 'carbohydrates_product': ' сыр фета', 'calories_product': ' сыр фета'},
                    {'mera': ' чеснок сушеный', 'weight': ' чеснок сушеный', 'protein_product': ' чеснок сушеный',
                     'fat_product': ' чеснок сушеный', 'carbohydrates_product': ' чеснок сушеный',
                     'calories_product': ' чеснок сушеный'},
                    {'mera': ' укроп', 'weight': ' укроп', 'protein_product': ' укроп', 'fat_product': ' укроп',
                     'carbohydrates_product': ' укроп', 'calories_product': ' укроп'},
                    {'mera': ' сметана 10% (нежирная)', 'weight': ' сметана 10% (нежирная)',
                     'protein_product': ' сметана 10% (нежирная)', 'fat_product': ' сметана 10% (нежирная)',
                     'carbohydrates_product': ' сметана 10% (нежирная)', 'calories_product': ' сметана 10% (нежирная)'},
                    {'mera': ' соус соевый', 'weight': ' соус соевый', 'protein_product': ' соус соевый',
                     'fat_product': ' соус соевый', 'carbohydrates_product': ' соус соевый',
                     'calories_product': ' соус соевый'},
                    {'mera': ' мандариновый сок', 'weight': ' мандариновый сок', 'protein_product': ' мандариновый сок',
                     'fat_product': ' мандариновый сок', 'carbohydrates_product': ' мандариновый сок',
                     'calories_product': ' мандариновый сок'},
                    {'mera': ' перец черный молотый', 'weight': ' перец черный молотый',
                     'protein_product': ' перец черный молотый', 'fat_product': ' перец черный молотый',
                     'carbohydrates_product': ' перец черный молотый', 'calories_product': ' перец черный молотый'},
                    {'mera': ' капуста пекинская', 'weight': ' капуста пекинская',
                     'protein_product': ' капуста пекинская', 'fat_product': ' капуста пекинская',
                     'carbohydrates_product': ' капуста пекинская', 'calories_product': ' капуста пекинская'},
                    {'mera': ' перец сладкий красный', 'weight': ' перец сладкий красный',
                     'protein_product': ' перец сладкий красный', 'fat_product': ' перец сладкий красный',
                     'carbohydrates_product': ' перец сладкий красный', 'calories_product': ' перец сладкий красный'},
                    {'mera': ' лук красный', 'weight': ' лук красный', 'protein_product': ' лук красный',
                     'fat_product': ' лук красный', 'carbohydrates_product': ' лук красный',
                     'calories_product': ' лук красный'}], 'portions': '6', 'calories_recipe': 'Калории: 106.3 ккал.',
       'protein_recipe': 'Белки: 8.7 гр.',
       'fat_recipe': 'Жиры: 6.3 гр.',
       'carbohydrates_recipe': 'Углеводы: 3.2 гр.',
       'ingredients': ['Курица и маринад:', 'Куриное филе - 200 гр.', 'Соевый соус - 1 ст.л.',
                       'Оливковое масло - 1 ст.л.', 'Перец черный молотый - 1/4 ч.л.', 'Черный кунжут - 1 ст.л.',
                       'Сырные шарики:', 'Сыр фета - 150 гр.', 'Чеснок сушеный - 1/2 ч.л.', 'Укроп - 15 гр.', 'Соус:',
                       'Сметана - 2 ст.л.', 'Соевый соус - 1 ст.л.', 'Сок мандарина - 30 мл.',
                       'Перец черный молотый - 1/4 ч.л.', 'Салат:', 'Пекинская капуста - 300 гр.',
                       'Перец болгарский - 1 шт.', 'Лук красный - 1/2 шт.']}
      )
