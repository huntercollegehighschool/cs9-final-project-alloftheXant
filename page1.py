#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.
import random
storylist = ["sharks", "sea turtles", "migration", "diving" ]
story = random.choice(storylist)
print("Lets play mad libs!")
if story == "sharks":
  place = str(input("Enter a place:"))
  adjective1 = str(input("Enter an adjective:"))
  color = str(input("Enter a color:"))
  country = str(input("Enter a country:"))
  adjective2 = str(input("Enter an adjective:"))
  size = str(input("Enter a size:"))
  job = str(input("Enter an occupation:"))
  time = str(input("Enter an increment of time:"))
  animal = str(input("Enter an animal:"))
  story = ("Researchers are warning beachgoers that they may not be the only ones headed to" + place + " this summer, as " + adjective1 + " " + color + " sharks are expected there, too. The warm weather in the northern" + country + "typically coincides with the migration of the " + adjective2 + " creatures to the Massachusetts area. Just know that " + size + " sharks are here, Atlantic White Shark Conservancy " + job + " Megan Winton said at a news conference on Wednesday, The Associated Press reported. They're a constant presence from June to fall. Winton's words of caution followed a great white sighting on Tuesday that resulted in Head of the Meadow Beach in Truro, Mass., being closed for a " + time + ". Locals were able to learn of the closure from the Atlantic White Shark Conservancy's Sharktivity app, which tracks confirmed and unconfirmed " + animal + " sightings.")
  print(story)

if story == "sea turtles":
  number = str(input("Enter a number:"))
  color = str(input("Enter a color:"))
  noun = str(input("Enter an abstract noun:"))
  adjective = str(input("Enter a comperative adjective:"))
  country = str(input("Enter a country:"))
  plant = str(input("Enter a plant"))
  animal = str(input("Enter an animal"))
  noun2 = str(input("Enter a plural noun:"))
  story = ("Sea Sense says its program has recorded and protected over " + number + " nests, and more than 528,000" + color + " and hawksbill turtle hatchlings have safely reached the sea to begin their long journey to " + noun + ". " + color + " turtles are the " + adjective + " common sea turtle species in " + country + ", feeding on extensive " + plant + " meadows found along the coast. According to Sea Sense, sea turtles in" + country + " are under threat as a result of centuries of " + animal + " exploitation for food, oil, leather and " + noun2 + ", as well as mortality associated with incidental capture in the fishing industry, marine and land-based pollution and degradation of foraging habitats. Infrastructure development and coastal erosion poses a significant threat to nesting beaches.")
  print(story)

if story == "migration":
  time = str(input("Enter a time of day:"))
  adjective = str(input("Enter an adjective:"))
  water = str(input("Enter a body of water (plural):"))
  direction = str(input("Enter a direction:"))
  star = str(input("Enter a star or planet:"))
  adjective2 = str(input("Enter a compartive adjective:"))
  year = str(input("Enter a year:"))
  tech = str(input("Enter a kind of technology:"))
  story = ("Every " +  time  + " at sundown, a great mass of mostly " + adjective + " sea creatures rises up from the depths into the topmost layers of the planet’s " + water + " . This daily vertical migration is the largest on Earth—an estimated 11 billion tons of animal biomass travels miles " + direction + " each night and then, before the " + star + " rises, returns back to the dimly lit “twilight zone” below. The animals make this journey to feed on the organic material closer to the water’s surface and do so at night to avoid being eaten by the " + adjective2 + " predators swimming there. The nighttime migration was first discovered in " + year + " by the U.S. Navy, whose new " + tech + " began pinging congregations of objects in the water column. Since then researchers, hobby divers and photographers have gone out to scuba dive at " + time + "and observe these nocturnal creatures.")
  print(story)

if story == "diving":
  place = str(input("Enter a place:"))
  animal = str(input("Enter an animal:"))
  water = str(input("Enter a body of water (plural):"))
  number = str(input("Enter a number:"))
  number2 = str(input("Enter another number:"))
  temp = str(input("Enter a temperature:"))
  organ = str(input("Enter an organ (plural):"))
  part = str(input("Enter a body part (plural):"))
  story = ("Whale sharks are one of a select group of large marine animals that scientists like Thorrold, of the Woods Hole Oceanographic Institution in " + place + ", have signed up as ocean-going research assistants. Fitted with electronic tags incorporating a suite of sensors, tracking devices and occasionally tiny cameras, they gather information where " + animal + " researchers can’t. They have revealed remarkable journeys across entire " + water + ", and they have shown that diving deep is pretty much ubiquitous among large marine predators of all kinds. Many regularly plunge " + number + "s and sometimes " + number2 + "s of meters — to depths where the water can be dangerously " + temperature + "and short of oxygen, there’s little or no light except for the flickers and flashes of bioluminescent organisms, and the pressure is immense, putting some animals at risk of fatal decompression sickness.To function at such depths, deep-diving species have evolved an array of anatomical and physiological adaptations — thick, insulating blubber, for instance, or blood vessels transformed into heat-exchange systems, collapsible " + organ + " and oxygen-storing muscles, and ultra-sensitive " + part + ".")
  print(story)