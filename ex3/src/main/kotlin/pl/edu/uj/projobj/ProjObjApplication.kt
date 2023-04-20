package pl.edu.uj.projobj

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
package com.raywenderlich.nftmarketplace.controller

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController // 1
class NftmarketplaceController {

  @GetMapping("/homepage")
  fun getHomePage() = "NFTs Marketplace"

  @GetMapping("/data")
  fun getData(): List<String> {
    return listOf("data1", "data2", "data3")
  }
}

@SpringBootApplication
class ProjObjApplication {
	
}

fun main(args: Array<String>) {
	runApplication<ProjObjApplication>(*args)
}
