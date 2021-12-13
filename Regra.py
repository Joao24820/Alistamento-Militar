while i < 18:
        print('Quem nasceu em {} tem {} anos em 2021'.format(n, i))
        a = 18-i
        print('Ainda faltam {} anos para o seu alistamento'.format(a))
        an = (2021 + a)
        print('seu alistamento será em {}'.format(an))
        break

    while i > 18:
        cal = 2021-n
        g = 2021+(18-i)
        print('Quem nasceu em {} tem {} anos em 2017'.format(n, cal))
        print('Voce deveria ter se alistado há {} anos'.format(cal-18))
        print('Seu alistamento foi em {}'.format(g))
        break

    while i == 18:
        gh = 2021-n
        print('Quem nasceu em {} tem {} anos em 2017 '.format(n, gh))
        print('Voce deve se alistar IMEDIATAMENTE!')
        break
