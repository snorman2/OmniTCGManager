package com.otcg.decks;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

@SpringBootApplication
@RestController
@Validated
public class DeckController {

	private DeckService deckService = new DeckService();

	public static void main(String[] args) {
		SpringApplication.run(DeckController.class, args);
	}

	@PostMapping("/create")
	public String createDeck(@RequestBody DeckModel newDeck){

		System.out.println(newDeck.getDeckName());
		System.out.println(newDeck.getClass());
		String response = deckService.createDeck(newDeck);
		return response;
	}

	@GetMapping("/deck")
	public DeckModel getDeck(@RequestParam(value = "id")  String id){

			int deckID = Integer.parseInt(id);
			return deckService.getDeck(deckID);
	}

	@PostMapping("/deck/update")
	public String updateDeck(@RequestParam(value = "id") String id, @RequestBody DeckModel updatedDeck){

		int deckId = Integer.parseInt(id);
		String updatedTcg = updatedDeck.getDeckTcg();
		ArrayList updatedCards = updatedDeck.getCards();

		return deckService.updateDeck(deckId, updatedTcg, updatedCards);
	}

	@GetMapping("/collection")
	public ArrayList<DeckModel> getCollection(){
		return deckService.getCollection();
	}


	@PostMapping("/deck/delete")
	public String deleteDeck(@RequestParam(value = "id") String id){
		int deckId = Integer.parseInt(id);
	return deckService.deleteDeck(deckId);
	}
}
