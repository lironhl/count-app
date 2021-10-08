from datetime import date

from yashish.server.schemas import InteractionType, YashishModel


class InteractionBase(YashishModel):
    date: date
    interaction_type: InteractionType

    happiness_level: int
    disappointment_level: int
    overall_level: int
    additional_description: str
    is_hungry: bool
    need_medicines: bool
    isolation_level: int

    user_id: int
    senior_id: int


class Interaction(InteractionBase):
    id: int

    user: "ShallowUser"


from yashish.server.schemas.users import ShallowUser  # noqa: E402

Interaction.update_forward_refs()
