package com.otcg.decks;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
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
	public ResponseEntity<String> createDeck(@Valid @RequestBody DeckModel newDeck){
		String response = deckService.createDeck(newDeck);
		return new ResponseEntity(response, HttpStatus.OK);
	}

	@GetMapping("/deck")
	public ResponseEntity getDeck(@RequestParam(value = "id")  int id){

			DeckModel deck = deckService.getDeck(id);
			if (deck == null || !(deck instanceof DeckModel)){
				String message = String.format("No deck with id %s exists", id);
				return new ResponseEntity<String>(message, HttpStatus.NOT_FOUND);
			}
			return new ResponseEntity<DeckModel>(deck, HttpStatus.OK);
	}

	@PostMapping("/deck/update")
	public ResponseEntity<String> updateDeck(@Valid  @RequestBody DeckModel updatedDeck){

		String updatedTcg = updatedDeck.getDeckTcg();
		ArrayList updatedCards = updatedDeck.getCards();
		String name = updatedDeck.getDeckName();
		int id = updatedDeck.getId();
		Boolean isUpdated = deckService.updateDeck(id, updatedTcg, name, updatedCards);

		if (!isUpdated){
			String message = String.format("There was a problem when updating the deck. Ensure the Id is valid and that the Tcg is the same. Id: %s Tcg: %s", id,updatedTcg);
			return new ResponseEntity(message, HttpStatus.NOT_FOUND);
		} else {
			String message = "Deck updated successfully.";
			return new ResponseEntity(message, HttpStatus.OK);

		}
	}

	@GetMapping("/collection")
	public String getCollection(){
		return "collection";
		//return deckService.getCollection();
	}


	@PostMapping("/deck/delete")
	public String deleteDeck(@RequestParam(value = "id") String id){
		int deckId = Integer.parseInt(id);
	return deckService.deleteDeck(deckId);
	}
}
