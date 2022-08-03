package com.otcg.api;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.otcg.decks.DeckModel;


import java.util.ArrayList;
import java.util.List;

public class ResponseModel {

    @JsonProperty(value = "deckList", required = true)
    DeckModel deckList;

    @JsonProperty(value = "collection", required = true)
    ArrayList<DeckModel> collection;

    public DeckModel getDeckList() {
        return deckList;
    }

    public void setDeckList(DeckModel deckList){
        this.deckList = deckList;
    }

    public ArrayList<DeckModel> getCollection() {
        return collection;
    }

    public void setCollection(ArrayList<DeckModel> collection) {
        this.collection = collection;
    }
}
