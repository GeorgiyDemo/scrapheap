<script>
	let name = "KOSHKA";
	let inputValue = "";
	let cats = ["cat1", "cat2"];

	let pos = {
		x: 0,
		y: 0
	};
	
	function changeNameHandler() {
		name = "Чета изменили"
	};

	function mouseMoveHandler(event){
		pos.x = event.x
		pos.y = event.y
	};

	function submitHandler(event){
		console.log(inputValue)
	}

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

	#mylabel {
		color: whitesmoke;

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

	.myclass {
		width: 400px;
		height: 200px;
		padding: 1rem;
		margin-bottom: 1rem;
		background-color: grey;
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

<button on:click={changeNameHandler}>Нажми меня</button>


<div class="myclass" on:mousemove={mouseMoveHandler}>
	<h2 id="mylabel">{pos.x}, {pos.y}</h2>
</div>


<form on:submit|preventDefault={submitHandler}>
	<input type="text" on:input={event => (inputValue = event.target.value)}>
	<button type="submit">Отправка</button>
</form>