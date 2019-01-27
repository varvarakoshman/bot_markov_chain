# bot_markov_chain

Данный бот моделирует марковскую цепь

**Принцип работы:** на вход подается фраза, в ответ ботом выдается его фраза (очень отдаленно похожая на разумный ответ)

**Ход работы:**
*  dataset

составляется dataset - текстовый файл с художественным текстом, количество слов - здесь: 263950, но лучше брать 500k+

dataset очищается от знаков препинания, обращений вида Mr./Mrs./Dr. и имен, стоящих в середине предложения
*  модель Маркова

по отфильтрованным данным создается модель Маркова k-го порядка (здесь: 3-го, но при тестах варьировали) (возможно, лучше взять 2-го)
модель Маркова k-го порядка - словарь с кортежем размера k в качестве ключа и словарем в качестве значения. 
В этом внутреннем словаре ключи - это слова, которые идут за упомянутым кортежем, а значения - их частота. 
С использованием этого словаря будут генерироваться предложения (здесь: все предложения не более 80 символов в сумме)
*  генерация предложений

 первое слово предложения выбирается случайно из множества всех первых слов из словаря, учитывая интонацию поданной на вход фразы. 
(те для ответа на вопрос первое слово будет выбираться из первых слов, следующих после вопросов. Аналогично с восклицанием и точкой)
Следующее слово выбирается случайным образом из заданного распределения потенциально следующих за текущим словом слов. При этом, задумка в том,
чтобы при выборе повысить приоритет тех слов, которые упоминаются в поданном на вход предложении (здесь: вероятность увеличивается в ~3 раза (варьировали))
Когда сгенерированное слово - знак препинания, накопившая цепочка слов присоединяется к ответу и, если длина этого ответа еще не превышает лимита (здесь: 80 символов),
будет генерироваться следующее предложение.

**Примеры общения:**
* me: why do we exist ?
* bot: Is what they say true after all that made you blush ? Why exactly.
* me: seems like you are the one who I mean really gets me
* bot: Quivocal tri quad and quinquivocal!
* me: well ok forget about that
* bot: Forget the whip! Forget yourself .
* me: what do you think of universe ?
* bot: What seems straight or crooked to us human beings.
* me: yeah like what do you think of it
* bot: Do not wish to speak anything worse of him
* me: him you mean god ?
* bot: You a goddam composition I said. Hasn’t he not created the world?
* me: what would you suggest me to do on weekends ?
* bot: Me myself and I. To need to know
* me: you are a phony !
* bot: where d you go with me. A toad ?
* me: i would go and make you smarter
* bot: Em good-by and send em postcards from hotels and all
* me: i am so bored !
* bot: It sounds terrible when you think about it.
* me: yeah right, and what do you think about ?
* bot: What calls itself a people today deserves no kings
* me: interesting idea, sadly not new at all
* bot: Just look! All believers! All too great happiness without envy!
* me: what’s up ?
* bot: A morning sun that emerges from dark mountains.
* me: not yet, only in four hours or something
* bot: So dark in here
* me: If you light up a lamp on a table it gets better .
* bot: It gets you. Better than your words can say your eyes tell me all your danger.
* me: I am thinking of good meal
* bot: Fires. Fires. Behold just now the most tender thoughts are coming to me ..
* me: In my case fires is a light of fridge, but you get me, yeah !
* bot: my river or tears ow course to you ! My own hatred because it stained you!
* me: no, please, don’t start again .
* bot: I don’t . Don’t even like to talk about while I sat down again.
* me: i am at home and i am in bed !
* bot: And i wondered what he'd tell when she saw i hadn't slept there or anything.
* me: i find pigeons so annoying in winter .
* bot: And snorted up rivers of tears. I sing and mock the fact that it's pretty safe.
* me: sun shines so bright in the morning !
* bot: You prefer the take it or leave it style of negotiating. The difference where i am?
* me: i have a problem with completing my project .
* bot: When i started doing something else.
* me: what can't you tell me ?
* bot: What your friend does while waking.
* me: who are you ?
* bot: I desire nothing from you who are merely willed. Are up on you you jesters! 
* me: no offense just curious .
* bot: I perish! Oh no! No harm.
* me: what do you prefer dogs or cats ?
* bot: What do you think? What i want they would not be permitted to want! 
* me: you seem to feel lonely, little piece of artiphicial intelligence ?
* bot: I can't tell you.
* me: you can trust me, believe me !
* bot: Indeed you deceive you contemplative ones! You the old the deep deep midnight? 
* me: why people call a bakery more than a bakery ?
* bot: Why you didn't like any more and you wanted to caress every monster. 
