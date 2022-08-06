package com.otcg.api.tcgs.mtg;

/**
 * <pre>
 *
 *  OTCG Manager
 *  File: MTGCardModel.java
 *
 *
 *  Description:
 *  Card Model class for MTG
 *
 * </pre>
 */

public class MTGCardModel {

    private String collectorNumber;
    private String name;
    private Object manaCost;
    private String type;
    private String subType;
    private String expansion;
    private String text;
    private int power;
    private int toughness;
    private int loyalty;
    private String rarity;

    public Object[] getInfo() {
        return new Object[]{collectorNumber, name, manaCost, type, subType, expansion, text, power, toughness, loyalty, rarity};
    }

    public String getCollectorNumber() {
        return collectorNumber;
    }

    public void setCollectorNumber(String collectorNumber) {
        this.collectorNumber = collectorNumber;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Object getManaCost() {
        return manaCost;
    }

    public void setManaCost(Object manaCost) {
        this.manaCost = manaCost;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getSubType() {
        return subType;
    }

    public void setSubType(String subType) {
        this.subType = subType;
    }

    public String getExpansion() {
        return expansion;
    }

    public void setExpansion(String expansion) {
        this.expansion = expansion;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }

    public int getToughness() {
        return toughness;
    }

    public void setToughness(int toughness) {
        this.toughness = toughness;
    }

    public int getLoyalty() {
        return loyalty;
    }

    public void setLoyalty(int loyalty) {
        this.loyalty = loyalty;
    }

    public String getRarity() {
        return rarity;
    }

    public void setRarity(String rarity) {
        this.rarity = rarity;
    }
}
