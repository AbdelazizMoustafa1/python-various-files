import os
import webbrowser
from datetime import date

today = date.today()

print("History of Covid-19 and Important contact details")

#HCMenu Function 
def HCMenu():
    # History and Contacts Menu to choose History of Covid-19 or Important contact details
    while True:
        os.system("clear")
        print('\n[History of Coronavirus - OR - Contact details]')
        print('1) History \n2) Contact Details')
        selection= input('Enter your Selection: ')

        if selection == '1':
           History()
        elif selection == '2':
           Contact_details() 
        else:
            print('Please select 1 or 2')
#end HCMenu

def History():
	print("Today's date:", today)
	print('\nCoronaviruses belong to the Coronaviridae family in the Nidovirales order. Corona represents crown-like spikes on the outer surface of the virus; thus, it was named as a coronavirus. Coronaviruses are minute in size (65–125 nm in diameter) and contain a single-stranded RNA as a nucleic material, size ranging from 26 to 32kbs in length. \n \nThe subgroups of coronaviruses family are alpha (α), beta (β), gamma (γ) and delta (δ) coronavirus. The severe acute respiratory syndrome coronavirus (SARS-CoV), H5N1 influenza A, H1N1 2009 and Middle East respiratory syndrome coronavirus (MERS-CoV) cause acute lung injury (ALI) and acute respiratory distress syndrome (ARDS) which leads to pulmonary failure and result in fatality. \n \nThese viruses were thought to infect only animals until the world witnessed a severe acute respiratory syndrome (SARS) outbreak caused by SARS-CoV, 2002 in Guangdong, China [1]. Only a decade later, another pathogenic coronavirus, known as Middle East respiratory syndrome coronavirus (MERS-CoV) caused an endemic in Middle Eastern countries')

	print('\nRecently at the end of 2019, Wuhan an emerging business hub of China experienced an outbreak of a novel coronavirus that killed more than eighteen hundred and infected over seventy thousand individuals within the first fifty days of the epidemic. This virus was reported to be a member of the β group of coronaviruses. The novel virus was named as Wuhan coronavirus or 2019 novel coronavirus (2019-nCov) by the Chinese researchers.')
	show_cases = input('\nOpen Live Cases Tracker? Yes or No: ')
	if show_cases == 'Yes':
		webbrowser.open('https://www.worldometers.info/coronavirus/')
	elif show_cases == 'No':
		print('Back to menu')


def Contact_details():
	print('\nThe health ministry’s Crisis Preparedness and Response Centre:')
	print('Hotlines: 03-8881 0200, 03-8881 0600 and 03-8881 0700 \nEmail address: cprc@moh.gov.my')

#Call the menu Function if history and contact details section was selected:
HCMenu()
