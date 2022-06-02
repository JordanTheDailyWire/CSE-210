class Director:

    def _get_inputs(self, cast):

        character = cast.get_first_actor("character")
        velocity = self._keyboard_service.get_direction()
        character.velocity = velocity

    def _do_updates(self, cast):

        character = cast.get_first_actor("character")
        artifacts = cast.get_actors("artifacts")
        rocks = cast.get_actors("rocks")

        max_x = self._video_service.width
        max_y = self._video_service.height
        cast.update(max_x, max_y)

        banner = cast.get_first_actor("banner")
        banner.text = "Score: " + str(character.score)

        for artifact in artifacts:
            if character.position == artifact.position:
                cast.remove_actor("artifacts", artifact)
                character.score += 1

        for rock in rocks:
            if character.position == rock.position:
                character.score -= 1
                cast.remove_actor("rocks", rock)