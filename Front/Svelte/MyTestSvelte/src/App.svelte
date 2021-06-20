<script>
	let name = "KOSHKA";
	let number = 11;
	let cats = ["cat1", "cat2"]
	let imgScr = "https://avatars.githubusercontent.com/u/16972045?v=4"
	let htmlString = "<b>Это текст</b>"
</script>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	img {
		width: 100;
		height: auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>


<h2>Кароч все работает {name.toLowerCase()}</h2>

<ul>
	{#each cats as cat}
		<li>{cat}
		</li>
	{/each}
</ul>

<img src={imgScr} alt="check"/>
<p>{@html htmlString}</p>