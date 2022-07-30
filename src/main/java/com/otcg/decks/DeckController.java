package com.otcg.decks;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

@SpringBootApplication
@RestController
@Validated
public class DeckController {

	private DeckService deckService;

	public static void main(String[] args) {
		SpringApplication.run(DeckController.class, args);
	}

	@PostMapping("/create")
	public String createDeck(@RequestBody int id, String name, String tcg, ArrayList cards){
		return deckService.createDeck(id, name, tcg, cards);
	}

	@GetMapping("/deck")
	public String getDeck(@RequestParam(value = "id", defaultValue = "0")  String id){

		try{
			Integer.parseInt(id);
			return String.format("Deck id is %s", id);
		} catch (NumberFormatException ex){
			return String.format("Invalid deck Id: %s", ex);
		}
	}

	@PostMapping("/deck/update")
	public String updateDeck(@RequestBody int id, String tcg, ArrayList newCards){
		return deckService.updateDeck(id, tcg, newCards);
	}

	@GetMapping("/decks")
	public String getAllDecks(){
		return "decks";
	}



}
